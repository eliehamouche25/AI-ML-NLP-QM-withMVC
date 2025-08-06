
from flask import Blueprint, render_template, request, redirect, url_for, flash
 
 
@ai_bp.route('/overview')
def ai_overview():
    return render_template('ai/overview.html')

@ai_bp.route('/models')
def ai_models():
    return render_template('ai/models.html')